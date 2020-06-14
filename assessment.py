machines = ["10XLarge","8XLarge","4XLarge","2XLarge","XLarge","Large"]
machine_capacity = {"Large":10,"XLarge":20,"2XLarge":40,"4XLarge":80,"8XLarge":160,"10XLarge":320}
NY_cost = {"Large":120,"XLarge":230,"2XLarge":450,"4XLarge":774,"8XLarge":1400,"10XLarge":2820}
India_cost = {"Large":140,"2XLarge":413,"4XLarge":890,"8XLarge":1300,"10XLarge":2970}
china_cost = {"Large":110,"XLarge":200,"4XLarge":670,"8XLarge":1180}
regions = {"New York":NY_cost,"India":India_cost,"China":china_cost}

#calculate total cost of a particular region
def cost_region(x,x_costs):
    sum = 0
    for i in range(0,len(x)):
        sum+=(x[i]*x_costs[i])
    return sum
 
#checking if cost is the minimym cost
def minimum_cost(i,units,cost,cost_dict):
    for j in range(i,len(machines)):
        key = machines[i]
        num = units // machine_capacity[key]
        if key not in cost_dict:
            continue
        if(num * cost_dict[key]) <cost:
            return False
    return True          
        
#resource_allocator    
def resource_allocator(hours,capacity):
    
    output = []        
    for i in regions:
        new_dict={}
        new_dict["region"] =i
        new_dict["total_cost"]=""
        new_dict["machines"] = []
        
        cap1= capacity
        machine_list = []
        cost_list =[]
        cost_dict = regions[i]
        for j in range(0,len(machines)):
            key= machines[j]
            
            if key not in cost_dict:
                continue
            
            
            num = cap1 // machine_capacity[key]
            cost = num * cost_dict[key]
        
            cap = num * machine_capacity[key]
            
            if not minimum_cost(j+1,cap,cost,cost_dict):
                num = 0
                cap = 0
            
            if num >0:
                new_dict["machines"].append((key,num))
            
            #remaining capacity
            cap1 -= cap
            machine_list.append(num)
            cost_list.append(cost_dict[key])
        machine_list.reverse() 
        cost_list.reverse()       
        cost =  cost_region(machine_list,cost_list) * hours
        new_dict["total_cost"] = "$"+str(cost)
        output.append(new_dict)
        
    return {"Output":output}
    
        
      
   

#print(resource_allocator(1,1150))
        
        
           
              
           
   
       
       
           
       
            
        
        
    

