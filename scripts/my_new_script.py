from envtest import summarize_csv_text

csv_text = """a,b,c
1,2,3
2,5,8
3,8,27
"""
print(summarize_csv_text(csv_text))
