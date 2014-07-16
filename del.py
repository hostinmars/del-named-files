import os
import sys
import re

def delSpecialNamingFiles(path, pattern, topdown=True):
    """ Delete the special named files
    You should indicate the path and specified pattern of file name.

    Example(Delete all files with '.' as prefix):
    del.py "E:\Tools" "^\..+"
    One more note: For python's command line you should use the double quote but single quote.
    For more details: http://stackoverflow.com/questions/16785475/python-command-line-args-format-issue
    """

    print 'Call delspecail files'
    if pattern == '':
        return None
    pat = re.compile(pattern)
    print 'start dir delspecail files'

    fileCount = 0;
    matchesCount = 0;
    with open('del.log', 'w') as log:
        log.write('$$>>Start process files\n>>with path: {p}\n>>with pattern: {p1}'.format(p=path, p1=pattern))
        log.write('\n---------------------------------------------------------------------------------\n')
        for root, dirs, files in os.walk(path):
            for name in files:
                fileName = os.path.join(root, name)
                fileCount = fileCount + 1;
                print fileName
                m = pat.match(name)
                if m:
                    matchesCount = matchesCount + 1;
                    os.remove(fileName)
                    print '{f} has been deleted'.format(f=fileName)
                    log.write('\n{f}'.format(f=fileName))
                    print '<-'

        log.write('\n---------------------------------------------------------------------------------\n')
        log.write('Total files: {n}\n'.format(n=fileCount))
        log.write('Match and DEL files: {n}\n'.format(n=matchesCount))


if __name__ == '__main__':
# Script starts from here
    if len(sys.argv) < 3:
        sys.exit()

    if sys.argv[1] == '--help' or sys.argv[1] == '-h':
        print 'Please fill all parameters to excute.'
        print 'The format as bellow:'
        print 'del [dir] [pattern]'
        sys.exit()

    path = sys.argv[1]
    pattern = sys.argv[2]
    print 'Start process dir: {p} with:'.format(p=path)
    print 'path: {p}'.format(p=path)
    print 'pattern: {p}'.format(p=pattern)
    delSpecialNamingFiles(path, pattern)
    print 'Completed!'
