
import java.io.File

fun byteArrayOfInts(vararg ints: Int) = ByteArray(ints.size) {
    pos -> ints[pos].toByte()
}

fun Byte.toPInt() = toInt() and 0xFF

fun main(args: Array<String>) {
    
    if (args.size > 1){
        val data = File(args[0]).readBytes()
        val offset = args[1].toIntOrNull()
        val dev = args[2].toIntOrNull()?:0
        if (data.size > 0 && offset != null && offset > 512){
            rebuild(data, offset, dev, args[1])
            println("-----Done-------")
        } else {
            println("Could not read from ${args[0]}")
        }
    } else {
        println("Specify the file name")
    }

    
}

fun rebuild(data: ByteArray, offset: Int, dev: Int, name: String){
    
    var output = byteArrayOfInts()
    
    println("Size: ${data.size}")

    var h = 0;
    for (x in 0 until 57600){
        if (data[x + offset].toPInt() > h){
            h = data[x + offset].toPInt()
        }
    }
    //h = 256
    println("H: $h")
    
    for (x in 0 until 57600){
        output += data[offset - (h * 2) + dev + (data[x + offset].toPInt() * 2)]
        output += data[offset - (h * 2) + dev + (data[x + offset].toPInt() * 2) + 1]
        
    }
    
    saveFile(output, name)
}


fun saveFile(output: ByteArray, name: String){
    val dir = File("extracted")
    
    if (!dir.exists()){
        dir.mkdirs()
        println("Created output folder")
    }
    val file = File(dir, "${name}_face.bin")
    file.createNewFile()
    file.writeBytes(output)
}
