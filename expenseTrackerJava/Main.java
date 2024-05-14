import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        //initialize ExpenseTracker with the filename, rough draft
        ExpenseTracker expenseTracker = new ExpenseTracker("ExpenseData.txt");

        System.out.println("Enter expense details:");
        System.out.print("Category: ");
        String category = scanner.nextLine();
        System.out.print("Amount: ");
        double amount = Double.parseDouble(scanner.nextLine().replace("$", ""));
        System.out.print("Date: ");
        String date = scanner.nextLine();

        //create the expense object after reading user input
        Expense expense = new Expense(category, amount, date);
        expenseTracker.addExpense(expense);
        expenseTracker.writeExpensesToFile(); //write expenses to file, rough draft

        System.out.println("Expenses:");
        expenseTracker.displayExpenses();
    }
}