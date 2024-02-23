// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

//datetime example in c#
DateTime employeeStartDate = new DateTime(2025, 03, 28);
DateTime today = DateTime.Today;
DateTime someDateTime = DateTime.Today; 
DateTime twoDaysLater = someDateTime.AddDays(2);
DayOfWeek day = someDateTime.DayOfWeek;

Console.WriteLine(someDateTime);

Console.ReadLine();
//bool isDST = someDateTime.IsDayLightSavingsTime();



