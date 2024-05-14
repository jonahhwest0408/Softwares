public class Expense extends Transaction {

    public Expense(String category, double amount, String date) {
        super(category, amount, date);
    }

    @Override
    public String getType() {
        return "Expense";
    }
}