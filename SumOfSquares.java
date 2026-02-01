import java.util.Scanner;

public class SumOfSquares {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of inputs: ");
        int n = scanner.nextInt();

        System.out.print("Enter the first number: ");
        int previousNumber = scanner.nextInt();

        int sum = 0;

        for (int i = 1; i < n; i++) {
            System.out.print("Enter the next number: ");
            int currentNumber = scanner.nextInt();

            int difference = currentNumber - previousNumber;
            sum += difference * difference;

            previousNumber = currentNumber;
        }

        System.out.println("Sum of squares of differences: " + sum);
    }
}

