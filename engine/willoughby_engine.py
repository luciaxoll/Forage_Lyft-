from engine.engine import Engine

class WilloughbyEngine(Engine):
    def __init__(self, current_milage, last_service_mileage):
        self.current_mileage = current_milage
        self.last_service_mileage = last_service_mileage

        def needs_service(self):
            return self.current_mileage - self.last_service_mileage > 60000
