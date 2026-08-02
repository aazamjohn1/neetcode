class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let stack = [];
        let valid_par = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }
 
    for (let char of s){
        if (char in valid_par){
           if(stack && stack[stack.length - 1] == valid_par[char]){
                    stack.pop()
           }else{
            return false
           }
        }else{
            stack.push(char)
        }
    
    
    }
    return stack.length == 0
}
}


  