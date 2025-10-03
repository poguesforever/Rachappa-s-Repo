#include <stdio.h>
int main(){
    int a;
    printf("Enter size of: ");
    scanf("%d", &a);

    int arr[a];
    
    printf("Enter %d elements:\n",a);
    for(int i=0;i<a;i++){
         scanf("%d",&arr[i]);
    } 

    for (int i=0;i<a/2;i++){
        int temp=arr[i];
        arr[i]=arr[a-i-1];
        arr[a-i-1]=temp;
    }

    printf("Reversed array:\n");
    for(int i=0;i<a;i++){
        printf("%d",arr[i]);
    }
    return 0;
}