def fitness_advice(predicted_loss):

    if predicted_loss < 0.5:
        return "Progress is slow. Increase workout time and protein intake."

    elif predicted_loss < 1.5:
        return "Good progress. Stay consistent and improve sleep."
    else:
        return "Excellent progress! Maintain routine and stay hydrated."