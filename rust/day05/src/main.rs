fn line_to_bin(line: String) -> String {
    line.replace("F", "0")
        .replace("B", "1")
        .replace("L", "0")
        .replace("R", "1")
}


fn bin_to_id(binary: &str) -> usize {
    let row = usize::from_str_radix(&binary[..7], 2).unwrap();
    let column = usize::from_str_radix(&binary[7..], 2).unwrap();
    row * 8 + column
}

fn task1() -> usize {
    let st_unconverted = std::fs::read_to_string("./input.txt").unwrap();
    let st_converted = line_to_bin(st_unconverted);
    let ids = st_converted.lines().map(|line| bin_to_id(line));
    ids.max().unwrap()
}

fn task2() -> usize {
    let st_unconverted = std::fs::read_to_string("./input.txt").unwrap();
    let st_converted = line_to_bin(st_unconverted);
    let mut ids: Vec<usize> = st_converted.lines().map(|line| bin_to_id(line)).collect();
    ids.sort();
    for i in 0..ids.len() {
        let this =ids[i];
        let next = ids[i+1];
        let next_expected = this + 1;
        if next_expected == next {
            continue
        } else {
            return next_expected
        }
    }
    panic!("Should exit earlier");
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
        panic!();
    }
    #[test]
    fn test_bench_2() {
        println!("task2: {}", bench(|| task2()));
        panic!();
    }
}
