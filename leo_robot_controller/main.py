from controller.movement_controller import MovementController
import keyboard

if __name__ == "__main__":
    controller = MovementController()
    controller.start()

    print("Press Esc to quit.")
    while True:
        if keyboard.is_pressed('esc'):
            print("Exiting...")
            break
