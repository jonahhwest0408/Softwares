//extra functionality, not implemented fully

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class ExpenseTracker {
    private List<Expense> expenses;
    private String filename;

    public ExpenseTracker(String filename) {
        this.filename = filename;
        this.expenses = new ArrayList<>();
        //load expenses from file when creating ExpenseTracker, rough draft
        readExpensesFromFile();
    }

    public void addExpense(Expense expense) {
        expenses.add(expense);
        //append new expense to the file, rough draft
        appendExpenseToFile(expense);
    }

    public void deleteExpense(Expense expense) {
        expenses.remove(expense);
        //update file after removing expense, rough draft
        writeExpensesToFile();
    }

    public void displayExpenses() {
        for (Expense expense : expenses) {
            System.out.println("Category: " + expense.getCategory() + ", Amount: " + expense.getAmount() + ", Date: " + expense.getDate());
        }
    }

    //read expenses from a file, rough draft
    public void readExpensesFromFile() {
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",");
                String category = parts[0];
                double amount = Double.parseDouble(parts[1]);
                String date = parts[2];
                Expense expense = new Expense(category, amount, date);
                expenses.add(expense);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    //write expenses to a file, rough draft
    public void writeExpensesToFile() {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(filename))) {
            for (Expense expense : expenses) {
                bw.write(expense.getCategory() + "," + expense.getAmount() + "," + expense.getDate());
                bw.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    //append a new expense to the file, rough draft
    private void appendExpenseToFile(Expense expense) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(filename, true))) {
            bw.write(expense.getCategory() + "," + expense.getAmount() + "," + expense.getDate());
            bw.newLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
