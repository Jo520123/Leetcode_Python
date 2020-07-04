class Solution:
    def simplifyPath(self, path):
        """
        :param path:  str
        :return:  str
        """
        output = []
        path_sep = path.split('/')
        for x in path_sep:
            if x:
                if x == '..':
                    if output:
                        output.pop()
                elif x == '.':
                    continue
                else:
                    output.append(x)

        out = '/' + '/'.join(output)

        return out
