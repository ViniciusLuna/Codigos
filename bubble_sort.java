import java.util.*;
public class bubble_sort{
    public static void main (String args[]){
        int X [] = new int [5];
        int n, i, aux;
        try (Scanner entrada = new Scanner(System.in)) {
            for ( i=0;i<=4;i++ ){
                System.out.println("Digite o" + (i+1) + "° número");
                X [i] = entrada.nextInt();
            }
        }

        for(n=1;n<=5;n++){
            for (i=0;i<=3;i++){
                if ( X [i] > X [i+1] ){
                    aux = X [i];
                    X [i] = X [i+1];
                    X [ i+1 ] = aux;
                }
            }
        }

        for (i=0;i<=4;i++){
            System.out.println((i+1)+"° núemro: "+X[i]);
        }
    }
}