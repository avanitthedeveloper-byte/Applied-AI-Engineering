# 10. Dictionary Methods

info = {
    "name" : "Avanit Kumar",
    "subjects" : [
        "Artificial Intelligence", 
        "Machine Learning",
        "Computer Network",
        "Operating System"
    ],
    "marks" : [
        98, 93, 92, 95
    ]
}

print(info.keys())
print(info.values())
print(info.items())
print(info.get("subjects"))

info.update({
    "city" : "Samastipur"
})

print(info.items())