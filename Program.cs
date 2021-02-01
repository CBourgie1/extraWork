using System;

namespace ClassEx
{
    class Program
    {
        static void Main(string[] args)
        {

            string macModelInput = "0";
            int macMemoryInput = 0;
            int macYearInput = 0;

            string dellModelInput = "";
            int dellMemoryInput = 0;
            int dellYearInput = 0;

            Console.WriteLine("Computer Price Evaluater");
            Console.WriteLine("Is your computer apple or dell");
            string userInput = Console.ReadLine();

            if (userInput == "apple")
            {
                Console.WriteLine("Enter the model of your computer");
                macModelInput = Console.ReadLine();

                Console.WriteLine("Enter the Ram of your computer");
                macMemoryInput = int.Parse(Console.ReadLine());

                Console.WriteLine("Enter the year of your computer");
                macYearInput = int.Parse(Console.ReadLine());

            }

            else if (userInput == "dell")
            {
                Console.WriteLine("Enter the model of your computer");
                dellModelInput = Console.ReadLine();

                Console.WriteLine("Enter the Ram of your computer");
                dellMemoryInput = int.Parse(Console.ReadLine());

                Console.WriteLine("Enter the year of your computer");
                dellYearInput = int.Parse(Console.ReadLine());
            }
            
            Computer macBook = new Computer();
            macBook.computerModel = macModelInput;
            macBook.computerMemory = macMemoryInput;
            macBook.computerYear = macYearInput;

            Computer Dell = new Computer();
            Dell.computerModel = dellModelInput;
            Dell.computerMemory = dellMemoryInput;
            Dell.computerYear = dellYearInput;

            if (userInput == "apple")
                Console.WriteLine($"Your computer value is: {macBook.DetermineComputerPrice()}");

            else if (userInput == "dell")
                Console.WriteLine($"Your computer value is: {Dell.DetermineComputerPrice()}");
        }
        
    }



    class Computer
    {
        public string computerModel { get; set; }
        public int computerMemory { get; set; }
        public int computerYear { get; set;}

        public int DetermineComputerPrice()
        {
            int computerValue = 0;

            if (computerModel == "apple") 
            {
                computerValue = 500;

                if (computerMemory >= 16)
                {
                    computerValue += 500;
                }
                else
                    computerValue += 300;

                if (computerYear >= 2019)
                {
                    computerValue += 500;
                }

                else computerValue += 200;

                return computerValue;
            }

            else if (computerModel == "dell")
            {
                computerValue = 400;

                if (computerMemory >= 16)
                {
                    computerValue += 400;
                }
                else
                    computerValue += 200;

                if (computerYear >= 2019)
                {
                    computerValue += 400;
                }

                else computerValue += 200;

                return computerValue;
            }

            return computerValue;
        }


    }
}
