import time

class TrafficLight:
    def __init__(self):
        self.state = "RED" # Start with Red for safety
        self.last_switch = time.time()
        self.min_duration = 2.0 # Minimum time to stay in state before switching (except emergency)

    def set_state(self, gesture):
        """
        Updates the traffic light state based on the detected gesture.
        Gesture Input:
        - STOP -> RED
        - GO -> GREEN
        - NEUTRAL -> Maintain current state (or maybe default logic)
        """
        current_time = time.time()
        
        # Simple Logic: Direct mapping with debounce/safety
        # If STOP, go RED immediately (safety priority)
        if gesture == "STOP":
            if self.state != "RED":
                print("Switching to RED (STOP Signal)")
                self.state = "RED"
                self.last_switch = current_time
        
        # If GO, go GREEN
        elif gesture == "GO":
            if self.state != "GREEN":
                # Ensure we don't rapid switch if we just turned RED? 
                # For now allow immediate switch on command
                print("Switching to GREEN (GO Signal)")
                self.state = "GREEN"
                self.last_switch = current_time
        
        # If NEUTRAL, do nothing (hold state)
        # In a real system, NEUTRAL might mean "auto mode" or "yellow" transition.
        # But per request: "synch with his signals", so we follow the signals.
        
        return self.state

    def get_color(self):
        """Returns the BGR color for visualization."""
        if self.state == "RED":
            return (0, 0, 255)
        elif self.state == "GREEN":
            return (0, 255, 0)
        elif self.state == "YELLOW":
            return (0, 255, 255)
        return (200, 200, 200) # Grey/Off
