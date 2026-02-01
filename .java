import java.util.Scanner;

class SeriesEvaluation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of terms (n): ");
        int n = scanner.nextInt();
        double sum = 0.0;

        for (int i = 1; i <= n; i++) {
            double term = calculateTerm(i); // replace with your series formula
            sum += term;
        }

        System.out.println("Sum of the series up to " + n + " terms: " + sum);
    }

    public static double calculateTerm(int i) {
        // replace with your series formula
        // for example: 1 + x + x^2 + x^3 + ...
        return Math.pow(i, 2); // example formula: i^2
    }
}