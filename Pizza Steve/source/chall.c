#include <stdio.h>

int main() {
   
    char encrypted_flag[] = "1HsBfq[|kQH2wAvRCHeiXR[PmtC72wAeL[iojvZhosASIX";
    
    
    
    for (int i = 0; encrypted_flag[i] != '\0'; i++) {
        
        char step1 = encrypted_flag[i] - 1;

        
        char original_char = step1 ^ 03;

        
        
    }
    
   printf("have a good day sir, do you know who is the most famous pizza in the world? ");
    return 0;
}
