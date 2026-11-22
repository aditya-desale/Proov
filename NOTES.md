# 

# \# Modernization Notes

# 

# I used an AI coding assistant to help modernize the fleet service project. I did not assume that every suggestion or result was automatically correct. I ran the existing tests after each major change and checked the output.

# 

# The original wear calculation used integer division, which caused a car at 14,900 km to be treated as having used zero complete service intervals. I checked that the corrected calculation flags it at the 80% threshold. I also checked that a missing last-service reading does not make a car appear due.

# 

# The report previously crashed when a car had no service reading and used integer division for average wear. These issues were corrected, and I added a regression test for the missing-reading case.

# 

# During the data analysis, I checked the breakdown and non-breakdown group averages. Kilometres since service, average daily kilometres, and load factor were higher in the breakdown group. Total odometer mileage and vehicle age were almost identical. I therefore did not use those two fields as risk indicators. The risk score is a relative ranking based on transparent weights, not a proven breakdown probability.

# 

# I also checked the kilometre-to-mile conversion and corrected the direction of the conversion. Finally, I ran the tests and the project verification script to check the changes.

# 

