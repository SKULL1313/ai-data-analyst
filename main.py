from analysis_tools import (
    calculate_total_revenue,
    revenue_by_product,
    calculate_average_transaction,
)


def answer_question(question):
    """Choose an analysis tool based on the user's question."""
    question = question.lower()
    
    if "total revenue" in question:
        total = calculate_total_revenue()
        return f"Total revenue is ${total:,.2f}."
    
    elif "average transaction" in question:
        average = calculate_average_transaction()
        return f"Average transaction value is ${average:,.2f}."
    
    elif "product" in question and "revenue" in question:
        results = revenue_by_product()
        best_product = results.idxmax()
        best_revenue = results.max()
        
        return (
            f"{best_product} generates the most revenue: "
            f"${best_revenue:,.2f}."
        )
        
    else:
        return (
            "I don't know how to answer that question yet. "
            "Try asking about total revenue, average transaction value, "
            "or product revenue."
        )
        

def main():
    print("AI Data Analyst Agent")
    print("-" * 35)
    print("Ask a business question, or type 'exit' to quit.")
    
    while True:
        question = input("\nYour question: ")
        
        if question.lower().strip() == "exit":
            print("Goodbye!")
            break
        
        answer = answer_question(question)
        print(f"Agent: {answer}")
        
    
if __name__ == "__main__":
    main()