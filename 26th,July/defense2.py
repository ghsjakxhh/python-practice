plans = {"basic": 15000, "standard": 25000, "premium": 39000, "family": 55000}

customer_inquiry = ["standard", "unlimited", "family", "basic"]

total = 0

for plan_name in customer_inquiry:
    try:
        print(f"The {plan_name} plan is {plans[plan_name]}.")
        total = total + plans[plan_name]
    except KeyError as A:
        print(f"Sorry. We don't have the {A} plan.")
    except Exception as B:
        print(f"A {B} was raised.")

print(total)

print(plans.get("student", "Sorry but we don't have the student plan."))