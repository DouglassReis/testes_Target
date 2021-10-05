using System;

namespace Target
{
    class Program
    {
        static void Main(string[] args)
        {
            int indice = 12;
            int k = 0;
            int soma = 0;

            while (k < indice)
            {
                k += 1;
                soma += k;
            }

            Console.WriteLine(soma);
        }
    }
}
