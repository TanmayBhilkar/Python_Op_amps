   int digitalRoot(char num[]){
    int len = strlen(num);
    int ans= 0;
    for(int i=0;i<len;i++){
        ans = 1 + ( ans + (num[i] - '0') - 1 ) % 9;
    }
    return ans;
}