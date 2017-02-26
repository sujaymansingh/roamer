"""
argh
"""
import os

class Engine(object):
    def __init__(self, original_dir, edit_dir):
        self.commands = []
        for digest, original_entry in original_dir.entries.iteritems():
            new_entry = edit_dir.find(digest)
            if new_entry is None:
                self.commands.append('rm %s' % original_entry.path)
            elif new_entry.name == original_entry.name:
                pass
            else:
                self.commands.append('cp %s %s' % (original_entry.path, new_entry.path))

        for digest, entry in edit_dir.entries.iteritems():
            if digest is None:
                self.commands.append('touch %s' % entry.path)

        unknown_digets = set(edit_dir.entries.keys()) - set(original_dir.entries.keys())

        for digest in unknown_digets:
            if digest is not None:
                raise Exception('digest %s not found' % digest)

    def print_commands(self):
        # sort so that cp comes first.  Need to copy before removals happen
        return '\n'.join(self.commands.sort())

    def run_commands(self):
        os.system(self.commands.sort())




            # original --> compare to new
            # digets found same name = nothing
            # digest found new name = mv
            # empty digest = new
            # digest missing... rm


            # """
            # digest not searched for = rm
            # find digest but name doesnt match  = copy from digest location to file(mv)
            # find digest and name match = do nothing
            # empty digest = touch new_file
            # not find digest = error
            # #####################

            # file name ends in / then is dir
            # """
