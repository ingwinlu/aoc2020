use std::fs::File;
use std::io::{self, BufRead};

const CUTOFF: u32 = 2020;

fn parse_in() -> Vec<u32> {
    let file = File::open("./input.txt").expect("read failed");
    let lines: Vec<u32> = io::BufReader::new(file)
        .lines()
        .map(|line| {
            line.expect("not a line")
                .parse::<u32>()
                .expect("not a number")
        })
        .collect();
    lines
}

pub fn task1() -> Result<u32, ()> {
    let lines = parse_in();
    for x in &lines {
        if x > &CUTOFF {
            continue;
        }
        for y in &lines {
            let sum = x + y;
            if sum == CUTOFF {
                let prod = x * y;
                // println!("{} + {} = {}, prod: {}", x, y, sum, prod);
                return Ok(prod);
            }
        }
    }
    Err(())
}

pub fn task2() -> Result<u32, ()> {
    let lines = parse_in();
    for x in &lines {
        if *x > CUTOFF {
            continue;
        }
        for y in &lines {
            if (x + y) >= CUTOFF {
                continue;
            }
            for z in &lines {
                let sum = x + y + z;
                if sum == CUTOFF {
                    let prod = x * y * z;
                    // println!("{} + {} + {} = {}, prod: {}", x, y, z, sum, prod);
                    return Ok(prod);
                }
            }
        }
    }
    Err(())
}

#[cfg(test)]
mod tests {
    // Note this useful idiom: importing names from outer (for mod tests) scope.
    use super::*;
    use easybench::bench;

    #[test]
    fn test_bench_1() {
        println!("task1: {}", bench(|| task1()));
    }
    #[test]
    fn test_bench_2() {
        println!("task2: {}", bench(|| task2()));
    }
}
