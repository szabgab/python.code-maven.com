
def transpose_text(text, width):
    result = []
    for i in range(width):
        for j in range(i, len(text), width):
            result.append(text[j])
    return "".join(result)
