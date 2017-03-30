#include<stdio.h>
#include<string.h>
 
void search(char *pat, char *txt);
int retNS(char *pat, int M, int state, int x);

int main()
{
  char *txt = "HONOLULU";
  char *pat = "LU";
  search(pat, txt);
  return 0;
}

int retNS(char *pat, int M, int state, int x)
{
  if (state < M && x == pat[state])
  return state+1;
 
  int ns, i; 
  for (ns = state; ns > 0; ns--){
    if(pat[ns-1] == x){
      for(i = 0; i < ns-1; i++){
        if (pat[i] != pat[state-ns+1+i])
          break;
      }
     if (i == ns-1)
       return ns;
    }
  }
 
  return 0;
}
 
void search(char *pat, char *txt)
{
  int M = strlen(pat);
  int N = strlen(txt);
 
  int TF[M+1][200], state, i;

  for (state = 0; state <= M; ++state){
    for (i = 0; i < 200; ++i){
      TF[state][i] = retNS(pat, M, state, i);
    }
  }
  
  state = 0;
  for (i = 0; i < N; i++){
    state = TF[state][txt[i]];
    if (state == M){
      printf ("\n Pattern found at index %d", i-M+1);
    }
  }
}
 
