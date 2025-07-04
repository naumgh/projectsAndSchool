package com.cooksys.ftd.assignments.collections.model;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

//import com.cooksys.ftd.assignments.collections.util.MissingImplementationException;

public class OrgChart {
	private Set<Employee> all_unique_employees = new HashSet<>();
	//private Map<Employee, Manager> employee_to_manager = new HashMap<>();
	private Map<Manager, Set<Employee>> worker_list = new HashMap<>();
	
	
    // TODO: this class needs to store employee data in private fields in order for the other methods to work as intended.
    //  Add those fields here. Consider how you want to store the data, and which collection types to use to make
    //  implementing the other methods as easy as possible. There are several different ways to approach this problem, so
    //  experiment and don't be afraid to change how you're storing your data if it's not working out!

    /**
     * TODO: Implement this method
     *  <br><br>
     *  Adds a given {@code Employee} to the {@code OrgChart}. If the {@code Employee} is successfully added, this
     *  method should return true. If the {@code Employee} was not successfully added, it should return false. In order
     *  to determine if and how an {@code Employee} can be added, refer to the following algorithm:
     *  <br><br>
     *  If the given {@code Employee} is already present in the {@code OrgChart}, do not add it and
     *  return false. Otherwise:
     *  <br><br>
     *  If the given {@code Employee} has a {@code Manager} and that {@code Manager} is not part of the
     *  {@code OrgChart} yet, add that {@code Manager} first and then add the given {@code Employee}, and return true.
     *  <br><br>
     *  If the given {@code Employee} has a {@code Manager} and the {@code Manager} is part of the {@code OrgChart},
     *  add the given {@code Employee} and return true.
     *  <br><br>
     *  If the given {@code Employee} has no {@code Manager}, but is a {@code Manager} itself, add it to the
     *  {@code OrgChart} and return true.
     *  <br><br>
     *  If the given {@code Employee} has no {@code Manager} and is not a {@code Manager} itself, do not add it
     *  and return false.
     *
     * @param employee the {@code Employee} to add to the {@code OrgChart}
     * @return true if the {@code Employee} was added successfully, false otherwise
     */
    public boolean addEmployee(Employee employee) {
    	if(employee == null) {
    		return false;
    	}
    	
        //employee already in org?
    	if(all_unique_employees.contains(employee)) {
    		return false;
    	}
    	
    	if(employee.hasManager()) {
    		Manager m = employee.getManager();
    		
    		if(!(all_unique_employees.contains(m))) {
    			addEmployee(m);
    			if(m.hasManager()) {
    				Manager top_m = m.getManager();
    				if(!worker_list.containsKey(top_m)) {
    					worker_list.put(top_m, new HashSet<>());
    				}
    				worker_list.get(top_m).add(m);
    			}
    			
    		}
    	
    		all_unique_employees.add(employee);
        	
        	if(!(worker_list.containsKey(m))) {
        		worker_list.put(m, new HashSet<>());
        	}
        	worker_list.get(m).add(employee);
        	return true;
    	
    	}else {
    		if(employee instanceof Manager) {
    			all_unique_employees.add(employee);
    			return true;
    		}else {
    			return false;
    		}
    	}
    	
    }

    /**
     * TODO: Implement this method
     *  <br><br>
     *  Checks if a given {@code Employee} has already been added to the {@code OrgChart}.
     *
     * @param employee the {@code Employee} to search for
     * @return true if the {@code Employee} has been added to the {@code OrgChart}, false otherwise
     */
    public boolean hasEmployee(Employee employee) {
    	if(all_unique_employees.contains(employee)) {
    		return true;
    	}else {
    		return false;
    	}
    }

    /**
     * TODO: Implement this method
     *  <br><br>
     *  Retrieves all {@code Employee}s that have been added to the {@code OrgChart} as a flat {@code Set}. If no
     *  {@code Employee}s have been added to the {@code OrgChart} yet, the returned {@code Set} should be empty (not
     *  {@code null}!).
     *
     * @return all {@code Employee}s in the {@code OrgChart}, or an empty {@code Set} if no {@code Employee}s have
     *         been added to the {@code OrgChart}
     */
    public Set<Employee> getAllEmployees() {
        if(all_unique_employees.isEmpty()) {
        	return new HashSet<>();
        }else {
        	return new HashSet<>(all_unique_employees);
        }
    }

    /**
     * TODO: Implement this method
     *  <br><br>
     *  Retrieves all {@code Manager}s that have been added to the {@code OrgChart} as a flat {@code Set}. If no
     *  {@code Manager}s have been added to the {@code OrgChart}, the returned {@code Set} should be empty (not
     *  {@code null}!).
     *
     * @return all {@code Manager}s in the {@code OrgChart}, or an empty {@code Set} if no {@code Manager}s
     *         have been added to the {@code OrgChart}
     */
    public Set<Manager> getAllManagers() {
        Set<Manager>managers = new HashSet<>();
        for(Employee e : all_unique_employees) {
        	if(e instanceof Manager) {
        		managers.add((Manager) e);
        	}
        }
        return managers;
    }

    /**
     * TODO: Implement this method
     *  <br><br>
     *  Retrieves all of the direct subordinates of a given {@code Manager} as a flat {@code Set}.
     *  <br><br>
     *  These are the {@code Employee}s (both {@code Worker}s and {@code Manager}s) that return the given
     *  {@code Manager} when their {@code .getManager()} method is called.
     *  <br><br>
     *  If the given {@code Manager} does not have any subordinates in the
     *  {@code OrgChart}, or if the given {@code Manager} is itself not in the {@code OrgChart}, the returned
     *  {@code Set} should be empty, but not {@code null}.
     *
     * @param manager the {@code Manager} whose direct subordinates need to be returned
     * @return all {@code Employee}s in the {@code OrgChart} that have the given {@code Manager} as a direct
     *         parent, or an empty set if the {@code Manager} is not present in the {@code OrgChart}
     *         or if there are no subordinates for the given {@code Manager}
     */
    public Set<Employee> getDirectSubordinates(Manager manager) {
        if(worker_list.containsKey(manager)) {
        	return new HashSet<>(worker_list.get(manager));
        }else {
        	return new HashSet<>();
        }
    }

    /**
     * TODO: Implement this method
     *  <br><br>
     *  Retrieves a full representation of this {@code OrgChart} as a {@code Map} of {@code Manager} keys and
     *  {@code Set<Employee>} values. Every single {@code Manager} in the {@code OrgChart} should appear as a key in
     *  the returned {@code Map}, and for each (@code Manager} key, every {@code Employee} (both {@code Worker}s and
     *  {@code Manager}s) in the {@code OrgChart} whose direct manager is that key should be in the associated
     *  {@code Set<Employee>} value.
     *  <br><br>
     *  Like the other methods, the return value of this method should not be {@code null} or contain {@code null},
     *  either in its keys or values. An empty {@code Map} should be returned if the {@code OrgChart} is empty.
     *
     * @return a map in which the keys represent the parent {@code Manager}s in the
     *         {@code OrgChart}, and the each value is a set of the direct subordinates of the
     *         associated {@code Manager}, or an empty map if the {@code OrgChart} is empty.
     */
    public Map<Manager, Set<Employee>> getFullHierarchy() {
        Map<Manager, Set<Employee>>res = new HashMap<>();
        for(Employee e: all_unique_employees) {
        	if(e instanceof Manager) {
        		Manager m = (Manager) e;
        		Set<Employee> subordinates;
        		if(worker_list.containsKey(m)) {
        			subordinates = new HashSet<>(worker_list.get(m));
        		}else {
        			subordinates = new HashSet<>();
        		}
        		res.put(m, subordinates);
        		
        	}
        }
        
        return res;
    }

}
