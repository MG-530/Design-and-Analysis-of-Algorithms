use std::io;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn recursive_combination(n: i32, k: i32) -> i64 {
    // Base cases
    if k == 0 || k == n {
        return 1;
    }
    if k > n {
        return 0;
    }
    
    // Recursive case
    recursive_combination(n - 1, k - 1) + recursive_combination(n - 1, k)
}

fn main() -> io::Result<()> {
    // Read input 
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);
    let mut lines = reader.lines();
    
    let n: i32 = lines.next().unwrap()?.trim().parse().unwrap();
    let k: i32 = lines.next().unwrap()?.trim().parse().unwrap();
    
    // Calculate result
    let result = recursive_combination(n, k);
    
    // Write output
    std::fs::write("output.txt", result.to_string())?;

    
    Ok(())
} 