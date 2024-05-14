public abstract class Transaction {
    private String category;
    private double amount;
    private String date;

    public Transaction(String category, double amount, String date) {
        this.category = category;
        this.amount = amount;
        this.date = date;
    }

    //abstract method to be implemented by subclasses
    public abstract String getType();

    //getters and setters
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public double getAmount() {
        return amount;
    }

    public void setAmount(double amount) {
        this.amount = amount;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
}
