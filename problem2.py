codes = ["BK103", "BK207", "BK103", "BK410"]

def book_position(codes, wanted):
    return codes.index(wanted)

assert book_position(codes, "BK207")
