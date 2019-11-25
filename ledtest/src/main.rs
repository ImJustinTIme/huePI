use rust_gpiozero::*;
use std::thread::sleep;
use std::time::Duration;

fn main() {
    let led = LED::new(18);
    
    loop{
        println!("on");
        led.on();
        sleep(Duration::from_secs(1));
        println!("off");
        led.off();
        sleep(Duration::from_secs(1));

    }
    
}
