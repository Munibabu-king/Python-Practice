s=['munibmuniabujgmjmunidsmjhmdms']
s=str(s)
s=list(s)
k=[s[i] for i in range(len(s)) if s[i].isalnum()]
print(sorted(k))
