import java.util.Scanner;

class Solution
{
	public static int SIZE = 50000;
	public static long triangleNumbers[] = new long [SIZE];
	public static void initializeTriangleNumbers()
	{
		triangleNumbers[1] = 1;
		triangleNumbers[2] = 2;
		for (int i = 3; i < SIZE; i++)
		{
			long sum = (i * (i + 1)) / 2;
			long answer = 1;
			int power = 0;
			while (sum % 2 == 0)
			{
				sum /= 2;
				power++;
			}
			answer *= power + 1;
			int j = 3;
			while (sum > 1)
			{
				power = 0;
				while (sum % j == 0)
				{
					sum /= j;
					power++;
				}
				answer *= power + 1;
				j += 2;
			}
			triangleNumbers[i] = answer;
		}
	}
	public static void main(String args[])
	{
		Scanner scanner = new Scanner(System.in);
		int testCases = scanner.nextInt();
		initializeTriangleNumbers();
		while (testCases-- > 0)
		{
			int N = scanner.nextInt();
			for (int i = 0; i < SIZE; i++)
				if (triangleNumbers[i] > N)
				{
					System.out.println((i * (i + 1)) / 2);
					break;
				}
		}
	}
}
