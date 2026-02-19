mars_multiple = 0.378

def main():
    weight_on_earth_str = input("Enter your weight: ")
    
    weight = float(weight_on_earth_str)
    
    weight_on_mars = weight * mars_multiple
    
    print("the weight on mars is " + str(weight_on_mars))
    
if __name__ == "__main__":
    main() 