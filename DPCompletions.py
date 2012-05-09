import os, fnmatch, re, threading, sublime, sublime_plugin

class ProjectCompletionsScan(threading.Thread):

    def __init__(self, rootPath, timeout):
        threading.Thread.__init__(self)
        self.rootPath = rootPath
        self.timeout = timeout
        self.result = None

    def run(self):
        try:
            patterns = ['.inc', '.php', '.module']
            search = re.compile(r'^function\s(.+?)\((?:(.+?))?\)\s{$', re.MULTILINE)
            compPath = os.path.dirname(self.rootPath) + '/Drupal.sublime-projectcompletions'
            cfp = open(compPath, 'w')
            cfp.close()
            cfp = open(compPath, 'a')

            for root, dirs, files in os.walk(os.path.dirname(self.rootPath)):
                for p in patterns:
                    for f in files:
                        if f.endswith(p):
                            # Open the file.
                            fp = open(os.path.join(root, f), 'r')
                            content = fp.read()
                            # Retrieve functions from file.
                            funcs = search.findall(content)
                            for row in funcs:
                                args = ''
                                if row[1]:
                                    i = 0
                                    arglist = row[1].replace(', ', ',').split(',')
                                    for i, val in enumerate(arglist):
                                        #arglist[i] = '${' + str(i + 1) + ':' + arglist[i].replace('$', '\$') + '}'
                                        arglist[i] = '${%s:%s}'   % (i + 1, arglist[i].replace('$', '\$'))
                                    args = '(%s)'   % (', '.join(arglist))
                                else:
                                    args = '()'
                                line = '%s\t%s%s' % (row[0], row[0], args)
                                # Append to file
                                cfp.write(line + "\n")
                            fp.close()
            cfp.close()
            return
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise


class ProjectCompletions(sublime_plugin.EventListener):

    def find_file(self, start_at, look_for):
        start_at = os.path.abspath(start_at)
        if not os.path.isdir(start_at):
            start_at = os.path.dirname(start_at)
        while True:
            for filename in os.listdir(start_at):
                if fnmatch.fnmatch(filename, look_for):
                    return os.path.join(start_at, filename) 
            continue_at = os.path.abspath(os.path.join(start_at, '..'))
            if continue_at == start_at:
                return None
            start_at = continue_at
    
    def on_post_save(self, view):
        path = view.file_name()
        rootPath = None

        if path:
            # Try to find the myproject.sublime-project file
            for filename in ['*.sublime-project']:
                rootPath = self.find_file(path, filename)
        if rootPath:
            threads = []
            thread = ProjectCompletionsScan(rootPath, 5)
            threads.append(thread)
            thread.start()

    def on_query_completions(self, view, prefix, locations):
        path = view.file_name()
        completions_location = None
        if path:
            # Try to find the Drupal.sublime-completions file
            for filename in ['*.sublime-projectcompletions']:
                completions_location = self.find_file(path, filename)
        if completions_location:
            fp = open(completions_location, 'r')

            t = ()
            data = []
            line = fp.readline()

            while len(line) != 0:
               e1, e2 = line.split("\t")
               t = e1, e2.rstrip()
               data.append(t)
               line = fp.readline()
               
            fp.close()
            return data
        else:
            return None