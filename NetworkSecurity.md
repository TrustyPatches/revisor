# Network Security #

## Questions ##

### Access Control ###



## Solutions ##

### Access Control ###

1. Reference Monitor: Access control component that refers to an abstract machine that mediates all accesses to objects by subjects.

2. Security Kernel: Firmware and software elements of a TCB that implement the reference monitor concept. It must verify all accesses, be protected from modification and be verifiable as correct.

3. Trusted Computing Base: The totality of protectinomechanisms within a computer system - including hardware, firmware and software - the combination of which is responsible for enforcing a security policy.

4. Integrity problem: The OS is not only the arbitrator of access requests, it is itself an object of access control. Not only this but we have to address two competing requirements: 1) users must be able to use (invoke) the OS but 2) they must not be able to *misuse* the OS.

5. There are two typical solutions to the integrity problem: 
    1) Modes of operation
    2) Controlled invocation

6. To protect itself an OS must be able to distinguish between computations on behalf of the OS and these on behalf of the user. 

7. Status flags allow the system to work in different modes; for example:
    - Intel 80x86 has two status bits and four modes
    - Unix distinguishes between user and superuser (root)

8. If a user wants to invoke a sensitive operation they willneed to switch to the correct mode of operation. This process is called controlled invocation.

9. Simply changing to superuser mode would give all superuser privileges to the user without any controls over what they actually do. Thus, the system should only perform a predefined set of operations in superuser mode and then return to user mode before handing control back to the user. 

10. x86 has two status bits to store the privilege level. Unix and Windows 2000 use ring 0 for OS and 3 for user mode.

11. Transfer of control occurs via 'gates'. Transfer of control is possible only to equal or lower rings. Processes can invoke subroutines only within their ring, they need 'gates' to execute procedures in an inner ring.

12. Information about system objects is stored in descriptors. The privilege level of an object is stored in the DPL field of its descriptors, stored in the descriptor table.

13. The OS can use a selector, a 16 bit field containing the index for the objects entry in the DT and a requested privilege level (RPL).

14. The code segment register stores the selector of the current process, access control decisions can be made by comparing CPL and DPL (subject -> object)

15. There is a problem in that a subroutine call saves state information about the calling process and return address on the stack. Should the stack be in the inner ring, which violates the policy forbidding write to an inner ring, or on the outer ring, which would leave it open to manipulation by the outer ring? Part of the stack (how much is described in the gates descriptor) is copied to a more prileged stack segment.

16. The confused deputy problem can be described like so: 
    - When invoking a subroutine through a gate, the CPL changes to the level of the code the gate is pointing to; on returning from the subroutine, the CPL is restored to that of the calling rocess. 
    - The outer ring process may ask the inner ring procesdure to copy an inner ring object to the outer ring.
    - This is known as a luring attack.
  To take into account this problem the ARPL (adjust requested privilege level) instruction can be used. This changes the RPL fields of all selectors to the CPL of the calling process.


