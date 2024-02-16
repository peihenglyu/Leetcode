class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        new_emails = []
        for email in emails:
            new_email = ""
            after_at = 0
            i = 0
            while i < len(email):
                if email[i] == '.' and not after_at:
                    pass
                elif email[i] == '+' and not after_at:
                    while email[i] != '@':
                        i += 1
                    new_email += (email[i])
                    after_at = 1
                elif email[i] == '@':
                    new_email += (email[i])
                    after_at = 1
                else:
                    new_email += (email[i])
                
                i += 1
                
            new_emails.append(new_email)
        
        return len(set(new_emails))
    
obj = Solution()
print(obj.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))