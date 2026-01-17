#Input "AI-953-kochi-delhi".
#Split and print details in proper case:
st="AI-953-kochi-delhi"
a=st.split("-")
print(a)
print(f"Airline:{a[0]}\nFlight:{a[1]}\nFrom:{a[2]}\nTo:{a[3]}")