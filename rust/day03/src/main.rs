use std::fs::File;
use std::io::{self, BufRead};

fn slope(step_down: usize, step_right: usize) -> u32 {
    let file = File::open("./input.txt").expect("file open failed");
    let lines: Vec<String> = io::BufReader::new(file)
        .lines()
        .map(|line| line.unwrap())
        .collect();

    let mut trees: u32 = 0;
    let mut y = 0;
    for line in lines.into_iter().step_by(step_down) {
        if line.chars().nth(y).unwrap() == '#' {
            trees += 1
        }
        y = (y + step_right) % 31;
    }
    trees
}

fn task1() -> u32 {
    slope(1, 3)
}

fn task2() -> u32 {
    slope(1, 1) * slope(1, 3) * slope(1, 5) * slope(1, 7) * slope(2, 1)
}

fn main() {
    println!("{}", task1());
    println!("{}", task2());
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
