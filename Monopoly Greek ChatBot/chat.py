from database import vector_store
results = vector_store.similarity_search_with_relevance_scores('Τα λευκά ζάρια γιατι χρησιμοποιούνται',k=2)
print(results)