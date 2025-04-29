# Load necessary libraries
library(dplyr)

# Step 1: Generate a list of 400 workers dynamically
set.seed(123)  # For reproducibility
num_workers <- 400

workers <- data.frame(
  ID = 1:num_workers,
  Name = paste("Worker", 1:num_workers, sep="_"),
  Gender = sample(c("Male", "Female"), num_workers, replace = TRUE),
  Salary = sample(5000:35000, num_workers, replace = TRUE)
)

# Step 2: Apply conditional statements and generate payment slips
workers <- workers %>%
  mutate(Employee_Level = case_when(
    Salary > 10000 & Salary < 20000 ~ "A1",
    Salary > 7500 & Salary < 30000 & Gender == "Female" ~ "A5-F",
    TRUE ~ "B2"  # Default level
  ))

# Step 3: Save payment slips to a CSV file
write.csv(workers, "payment_slips.csv", row.names = FALSE)

print("Payment slips generated successfully!")

