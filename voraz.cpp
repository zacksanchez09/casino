#include<iostream>
#include<conio.h>
#include <cstdlib>

using namespace std;

int main() {
int n;
int arc;
int importe, pago;
int cambio = 0;
cout<<"Ingrese la cantidad de monedas a usar:"<<endl;
cin>>n;
system("cls");
int monedas[n], contadores[n], cont=0;
cout<<"Ingrese sus valores: "<<endl;
for(int i=0;i<n;i=i+1){
    cin>>monedas[i];
    contadores[i]=0;
    cout<<" "<<endl;
}
for(int i=0;i<n;i++)
  for(int j=i+1;j<n;j++)
      if(monedas[i]<monedas[j]){
          arc=monedas[i];
          monedas[i]=monedas[j];
          monedas[j]=arc;
      }
cout<<" "<<endl;
system("cls");
cout<<"Estas son Tus Monedas"<<endl;
for (int i=0;i<n;i++){

    cout<<monedas[i]<<endl;

}
getch();
system("cls");
cout<<"Importe a pagar:"<<endl;
cin>>importe;
cout<<"Pagar con:"<<endl;
cin>>pago;
system("cls");
cambio=pago-importe;
cout<<"pagar:"<<importe<<".00 pesos con "<<pago<<".00 pesos su cambio es "<<cambio<<endl;
cont=0;
do{
  if(monedas[cont]<=cambio){
    cambio=cambio-monedas[cont];
    contadores[cont]=contadores[cont]+1;
  }
  else{
    cont++;
  }
}while(cambio!=0);
  cout<<"Se usaron estas monedas:"<<endl;
  for (int i=0;i<n;i++){
    cout<<"moneda de $"<<monedas[i]<<"pesos se uso "<<contadores[i]<<" veces"<<endl;
  }

  return 0;
}
