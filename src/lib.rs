#[no_mangle]
pub extern fn hello_rust_ptr() -> *const u8 {
    "Hello, world!\0".as_ptr()
}

#[no_mangle]
pub extern fn hello_rust() {
    println!("hello world");
}
