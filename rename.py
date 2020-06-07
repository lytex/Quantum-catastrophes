for file in ["classical.py", "quantum.py"]:
    with open(file) as f:
        content = f.read()
    content = content.replace("Λ", "Lambda")
    content = content.replace("Δ", "d")
    content = content.replace("ρ", "rho")
    content = content.replace("ϕ", "phi")
    with open("ascii_" + file, "w") as f:
        f.write(content)
