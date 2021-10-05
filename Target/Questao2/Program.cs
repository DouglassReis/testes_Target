using System;

namespace Questao2
{
    class Program
    {
        static void Main(string[] args)
        {
            long number = long.Parse(Console.ReadLine());

            if (Fibonnaci(number))
            {
                Console.WriteLine("O número pertence a sequência de Fibonacci");
            }
            else
            {
                Console.WriteLine("O número NÃO pertence a sequência de Fibonacci");
            }
         }

        static bool Fibonnaci(long number)
        {
            long n1 = 0;
            long n2 = 1;
            long aux;
            bool validador = (number == 0 || number == 1) ? true : false;

            while (n2 < number)
            {
                aux = n2;
                n2 += n1;
                n1 = aux;
                if (n2 == number)
                {
                    validador = true;
                }
                
            }
            return validador;
        }
    }
}
