class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        for i in range(len(command)):
            if i+1 < len(command) and  command[i] == "(" and command[i+1] == ")":
                result += "o"
            else:
                if command[i] != "(" and command[i] !=")":
                    result += command[i]
        return result 
            

       
                