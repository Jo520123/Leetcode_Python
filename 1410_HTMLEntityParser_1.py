class Solution:
    def entityParser(self, text):
        """
        :param text: str
        :return: str
        """


        d = {"&quot;" : '"', "&apos;" : "'", "&amp;" : "&", "&gt;" : ">", "&lt;" : "<" , "&frasl;" : "/"}

        for x, y in d.items():
            text = text.replace(x,y)

        return text
