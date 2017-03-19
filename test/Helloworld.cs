using System;

public static class HelloWorld
{
    public static void Main(string[] args)
    {
    	foreach(var arg in args)
    	{
        Console.WriteLine(arg);
    	}
    }
}
